using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class GameManager : MonoBehaviour
{
    public int maxMessage = 10;

    public GameObject chatPanel, textObject;
    public InputField chatBox;
    [SerializeField]
    List<Message> messageList = new List<Message>();

    void Start()
    {
        
    }

    void Update()
    {
        if(chatBox.text != "")
        {
            if (Input.GetKeyDown(KeyCode.Return))
            {
                SendMesToChat($"You Said: {chatBox.text}");
                ChatBot(chatBox.text);
                chatBox.text = string.Empty;
            }
        }
           
        if (!chatBox.isFocused)
        {
            if (Input.GetKeyDown(KeyCode.Space))
            {
                SendMesToChat("You press space");
                Debug.Log("Space");
            }
        }
            
            
    }
    public void ChatBot(string text)
    {
        if (text == "Hello")
        {
            SendMesToChat("Bot: Hello!");
        }
    }
    public void SendMesToChat(string text)
    {
        if (messageList.Count >= maxMessage)
        {
            Destroy(messageList[0].textObject.gameObject);
            messageList.Remove(messageList[0]);
        }
        Message newMessage = new Message();

        newMessage.text = text;

        GameObject newText = Instantiate(textObject, chatPanel.transform);

        newMessage.textObject = newText.GetComponent<Text>();

        newMessage.textObject.text = newMessage.text;

        messageList.Add(newMessage);
    }

}

[System.Serializable]
public class Message
{
    public string text;
    public Text textObject;
}