# OpenAI-API-demo
A demo about APIs for OpenAI, including Fine-tunes. This demo is for testing and demonstration purposes only and should not be used in a production environment.


# How to use

## 1. Use VSC

I strongly recommend using visual studio code to open the project, your project structure should be like this:

```
.
├── LICENSE
├── README.md
├── common.py
├── config.example.yaml
├── config.yaml
├── fine_tuning.py
├── ignore
│   ├── 1.json
│   ├── temp.py
│   └── prompts
│       ├── fine_tuning.jsonl
│       ├── fine_tuning.md
│       └── fine_tuning.md.jsonl
├── prompts
│   ├── fine_tuning.jsonl
│   ├── fine_tuning.md
│   └── fine_tuning.md.jsonl
└── tools
    └── tool_convert_md_to_jsonl.py
```

I recommend adding a `ignore` folder to root dir, because it is used to store temporary files, and it is not necessary to upload to github.

Remember that config.yaml and any files in ignore folder should not be uploaded to github. They have been added to .gitignore.

## 2. Config

Copy `config.example.yaml` to `config.yaml`, then add your API key to config.yaml.

Add proxy if you need.

## 3. Prepare prompts

If you already have prompts, you can put them to `ignore/prompts/fine_tuning.jsonl` folder.

## 4. Run

Run `fine_tuning.py` to start fine-tuning or manage your fine-tuning files, jobs ,and models.

# Other Tools

## Convert markdown to jsonl

1. Use `tool_convert_md_to_jsonl.py` to convert markdown to jsonl.

2. Prepare a markdown file, like `fine_tuning.md`, then run `tool_convert_md_to_jsonl.py`, it will generate `fine_tuning.md.jsonl` in the same folder.

3. Copy `fine_tuning.md.jsonl` to `ignore/prompts/fine_tuning.jsonl` file for fine-tuning.

4. Or you can do any customer process to get your prompts.

# Reference

> https://platform.openai.com/docs/api-reference/fine-tunes


# License

[MIT License](LICENSE)