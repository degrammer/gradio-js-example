import gradio as gr
import subprocess

blocks = gr.Blocks()


def start(command):
    with blocks as demo:
        subject = gr.Textbox(placeholder="subject")
        verb = gr.Radio(["ate", "loved", "hated"])
        object = gr.Textbox(placeholder="object")

        with gr.Row():
            btn = gr.Button("Create sentence.")
            reverse_btn = gr.Button("Reverse sentence.")
            foo_bar_btn = gr.Button("Append foo")
            reverse_then_to_the_server_btn = gr.Button(
                "Reverse sentence and send to server."
            )

        def sentence_maker(w1, w2, w3):
            return f"{w1} {w2} {w3}"

        output1 = gr.Textbox(label="output 1")
        output2 = gr.Textbox(label="verb")
        output3 = gr.Textbox(label="verb reversed")
        output4 = gr.Textbox(
            label="front end process and then send to backend")

        btn.click(sentence_maker, [subject, verb, object], output1)
        reverse_btn.click(
            None, [subject, verb, object], output2, _js=f"{command}"
        )
        verb.change(lambda x: x, verb, output3,
                    _js="(x) => [...x].reverse().join('')")
        foo_bar_btn.click(None, [], subject, _js="(x) => x + ' foo'")

        reverse_then_to_the_server_btn.click(
            sentence_maker,
            [subject, verb, object],
            output4,
            _js="(s, v, o) => [s, v, o].map(x => [...x].reverse().join(''))",
        )

    demo.launch()


file_paths = ['reverseWords']
if file_paths:
    print(f"Procesing files:{file_paths}")
    for file in file_paths:
        print(f"Opening file {file}")
        with open(f"./out/{file}.js") as functionFile:
            start(command=functionFile.read())
