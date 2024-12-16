
# 🔗 Simple URL Shortener  

## 🚀 Project Overview  

This project is a **URL Shortener** service that takes long URLs and generates shortened links for easy sharing. When a shortened link is accessed, users are seamlessly redirected to the original URL.  

This project was built as part of my **internship at CodeAlpha** to strengthen my backend development skills.  

---

## ⚙️ **Tech Stack**  

- **Backend Framework**: Flask (Python)  
- **Database**: SQLite / Any preferred database  
- **Testing**: Manual testing with Postman & browser  

---

## 💡 **Features**  

1. **Shorten URLs**: Convert long URLs into shorter, shareable links.  
2. **Redirect**: Accessing the shortened link redirects users to the original URL.  
3. **Database Integration**: All mappings of original and shortened URLs are stored efficiently.  
4. **Error Handling**: Proper validation and error messages for invalid URLs or missing parameters.  

---

## 📽️ **Video Demo**  

Watch the **source code walkthrough** and project demonstration here:  
[![Watch the Video](https://img.shields.io/badge/Click%20Here-Video%20Demo-red)](./media/Overview.mp4)  

---

## 🚀 **How to Run the Project**  

### 1. Clone the Repository  

```bash
git clone https://github.com/elqabasy/CodeAlpha_URL_Shortener.git
cd simple-url-shortener
```

### 2. Set Up the Virtual Environment  

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies  

```bash
pip install -r requirements.txt
```

### 4. Run the Application  

```bash
python app.py
```

The server will start at `http://127.0.0.1:5000/`.

---

## 🛠️ **Endpoints**  

### 1. Shorten URL  

- **Endpoint**: `/shorten`  
- **Method**: POST  
- **Payload**:  

    ```json
    { "original_url": "https://example.com" }
    ```  

- **Response**:  

    ```json
    { "short_url": "http://127.0.0.1:5000/short/<generated_id>" }
    ```  

### 2. Redirect to Original URL  

- **Endpoint**: `/short/<generated_id>`  
- **Method**: GET  
- **Description**: Redirects to the original URL.  

---

## 🎯 **Project Goals**  

- Learn and implement **URL redirection logic**.  
- Integrate backend services with **Flask** and **databases**.  
- Improve skills in building RESTful APIs.  

---

## 📝 **License**  

This project is licensed under the MIT License.  

---

## 🤝 **Connect with Me**  

If you have any suggestions or feedback, feel free to reach out:  

- **LinkedIn**: [Mahros AL-Qabasy](www.linkedin.com/in/ma7ros)  
- **GitHub**: [elqabasy](https://github.com/elqabasy)  
