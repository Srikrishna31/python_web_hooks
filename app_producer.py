from flask import Response, render_template
from init_producer import app
import tasks_producer
from typing import Any, Dict

def stream_template(template_name: str, **context: Dict[str, Any]) -> Any:
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    rv.enable_buffering(5)
    return rv


@app.route("/", methods=["GET"])
def index() -> str:
    import os
    print (os.getcwd())
    return render_template('producer.html')

@app.route("/producetasks", methods=["POST"])
def producetasks() -> Response:
    print("producetasks")
    return Response(stream_template('producer.html', data=tasks_producer.produce_bunch_of_tasks()))

if __name__=="__main__":
    app.run(host="localhost", port=5000, debug=True)