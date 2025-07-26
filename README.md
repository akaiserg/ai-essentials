
## 🔄 Adding New Tools

To add a new tool to the OpenAI Tool Agent:

1. **Define the function**:
   ```python
   def your_new_tool(param: str) -> str:
       """Your tool description"""
       # Your implementation
       return result
   ```

2. **Add to available_tools**:
   ```python
   available_tools = {
       "get_temperature": get_temperature,
       "your_new_tool": your_new_tool,
   }
   ```

3. **Add tool definition**:
   ```python
   tools = [
       # ... existing tools
       {
           "type": "function",
           "function": {
               "name": "your_new_tool",
               "description": "Description of what your tool does",
               "parameters": {
                   "type": "object",
                   "properties": {
                       "param": {
                           "type": "string",
                           "description": "Parameter description"
                       }
                   },
                   "required": ["param"],
               },
           }
       },
   ]
   ```

## 🧪 Development

### Installing new dependencies
```bash
uv add package_name
```

### Removing dependencies
```bash
uv remove package_name
```

### Installing development tools
```bash
uv tool install black  # Code formatter
uv tool install ruff   # Linter
```

## 📝 API Reference

### OpenAI Models Used
- **gpt-4o**: Latest OpenAI model with function calling capabilities

### Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key (required)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- OpenAI for their powerful API
- The uv team for the excellent package manager
- Python community for the amazing ecosystem