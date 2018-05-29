from nltk.tokenize import word_tokenize,sent_tokenize
from TextCleaner import TextCleaner
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from pprint import pprint
some_string="Class Action Lawsuit Seeks Court-Ordered Hard Fork In a new twist in the BitGrail saga, Nano is being sued.    Simon Golstein  |  News ( CryptoCurrency )  |   Sunday, 08/04/2018 | 13:00 GMT   Photo: FMShare this articleA class action lawsuit is seeking a court-ordered hard fork of a cryptocurrency – if the suit is successful, it will be unprecedented.Most interesting/novel part of this new class action involving Nano/XRB is the demand that the court order a “rescue fork.” First time I think, but will not be the last. pic.twitter.com/lWmfCokHo2Join our Telegram channel and get all the latest cryptocurrency news directly to your phone!— Palley (@stephendpalley) April 6, 2018BackgroundThe cryptocurrency in question is called XRB, which comes from a blockchain called Nano. The lawsuit concerns $150 million worth of XRB tokens being stolen from Italian cryptocurrency exchange BitGrail in February. BitGrail and Nano both blame each other for the hack.As we reported at the time, the operator of BitGrail, Francesco “The Bomber” Firano, drew ire because his handling of the exchange leading up to the theft seemed suspicious, and his reaction in the aftermath of the theft left much to be desired.The only currency stolen from the exchange was XRB. Evidence suggested that the money was stolen because of shortcomings in the exchange’s security systems. This was certainly the attitude taken by Nano, which contacted the authorities as soon as it was informed of the theft and published a statement distancing itself from BitGrail.Bitgrail continues to blame the theft on a malfunction in Nano’s software.Hard forkNow, the thing that most angered users of the exchange was the fact that Firano made it clear that BitGrail would not be able to repay them, because it simply didn’t have the money.One solution would have been for Nano to undergo a hard fork. A hard fork is an upgrade of a blockchain, so called because the chain can be visualised as splitting into two paths. Users receive the new version of the cryptocurrency equal to the amount of the old version held at that moment, and the old version becomes unusable (if the fork is accepted – but that’s another story). By doing this, victims of the BitGrail hack would have had their funds restored.Nano’s response to this request: “An option suggested by Firano was to modify the ledger in order to cover his losses — which is not possible, nor is it a direction we would ever pursue.”Firano thus attempted to switch blame to Nano:NANO on BitGrail have been stolen.Unfortunately there is no way to give it back to you at 100% (we only got 4 MLN XRN right now).The devs, as you have guessed, dont want to collaborate— Francesco The Bomber (@bomberfrancy) February 9, 2018The exchange closed immediately after the hack, but has since reopened with a less-than-promising plan to repay customers.The twistUsers of BitGrail had been discussing a lawsuit against the exchange even before the hack, because withdrawals has been suspended. Not only was this a violation of the exchange’s terms of service, they suspected that the exchange was looking to manipulate the price of XRB; at the time, the exchange handled about 75 percent of all XRB transactions, and the largest exchange in the world had recently announced that it would be listing XRB in the near future. They used Reddit to discuss a class action suit, planning to use a law firm called Silver Miller Law.But in the end, it is Nano being sued… and by the very same law firm.Why?Basically, NANO knew of the issues being faced by BitGrail. The fact that it continued its association with a faulty exchange makes it at least partly complicit in the security failings. The law firm says in its press release:“Silver Miller has commenced a new class action lawsuit on behalf of investors in NANO f/k/a RaiBlocks (XRB), alleging that NANO and key members of its core team violated federal securities laws and that, in their push to introduce XRB to a wide market of investors, recklessly directed investors to open accounts and place their assets with a little known, and severely troubled, Italian cryptocurrency exchange called BitGrail..” googletag.cmd.push(function() { googletag.display('inside_article_MPU'); }); Share this article Tags: Bitgrail / cryptocurrency / hack / hard fork / lawsuit / nanoRelated News Exclusive: Facebook to Launch its Own Cryptocurrency with Massive ICO  Mayor of Seoul Announces City Cryptocurrency  BitGrail Denies Responsibility for Hack, Will Refund Coins “Voluntarily”  Got a news tip? Let Us Know  Found a mistake? Let us know  googletag.cmd.push(function() { googletag.display('LB_2'); });  Leave a Reply Be the First to Comment!Notify of new follow-up commentsnew replies to my comments              Notify of new replies to this comment           Notify of new replies to this comment  "
#NO TEXT CLEANING
ps = PorterStemmer()
wnl = WordNetLemmatizer()
tc=TextCleaner(txt=some_string)
tc.clear_text_base()
tc.clear_special_char()
some_string=tc.get_text()

#WITH TEXT CLEANING


stop_words = set(stopwords.words("english"))

words = word_tokenize(some_string)

filtered_sentence = []

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

# print(filtered_sentence)

# stemmed=[]

lemmatized=[]

for w in filtered_sentence:
    lemmatized.append(wnl.lemmatize(w))
    # stemmed.append(ps.stem(w))

print("filtered_sentence","lemmatized","stemmed")
print(len(filtered_sentence))
print(len(lemmatized))
# print(len(stemmed))

