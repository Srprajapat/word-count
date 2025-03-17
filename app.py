from flask import Flask, request, jsonify, render_template
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def map_function(text_chunk, result_list, index):
    word_count = {}
    words = text_chunk.split()
    for word in words:
        word = word.lower()
        word_count[word] = word_count.get(word, 0) + 1
    result_list[index] = word_count
    print("thread:",threading.get_ident(),index,word_count)

def reduce_function(mapped_data):
    final_count = {}
    for partial_count in mapped_data:
        for word, count in partial_count.items():
            final_count[word] = final_count.get(word, 0) + count
    return final_count

@app.route('/wordcount', methods=['POST'])
def word_count():
    data = request.json
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    
    text = data['text']
    chunks = text.split('\n') 
    
    results = [None] * len(chunks)
    threads = []
    
    for i, chunk in enumerate(chunks):
        thread = threading.Thread(target=map_function, args=(chunk, results, i))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    final_word_count = reduce_function(results)
    
    return jsonify(final_word_count)

if __name__ == '__main__':
    app.run(debug=True)
