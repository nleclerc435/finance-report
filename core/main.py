import finance
import mail
import converthtml

if __name__ == "__main__":
    for s in finance.stocks:
        finance.plot_data(s)
    converthtml.get_final_html()
    mail.send_report()