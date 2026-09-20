# Gera as páginas legais do Sextant (política de privacidade + termos) em vários idiomas.
# Preencha os dados abaixo e rode: python3 build.py
import html, sys

CONFIG = {
    "NAME": "Valmir Araújo de Lima",
    "EMAIL": "{{EMAIL}}",      # e-mail público de contato para privacidade
    "BUSINESS": "{{NOME DA EMPRESA}}",  # nome da empresa (enkeltpersonforetak)
    "ORGNR": "{{ORG.NR}}",              # organisasjonsnummer (9 dígitos, Brønnøysundregistrene)
    "DATE": "2026-09-20",
}

# Cada seção: (título, [parágrafos ou ("ul", [itens])])
L = {}

L["pt"] = dict(
 lang="pt-BR", label="Português", title="Sextant — Privacidade e Termos", updated="Atualizado em",
 privacy=("Política de Privacidade", [
  ("1. Quem somos", ["O Sextant é um aplicativo náutico (mapa de barcos, peças e serviços, ferramentas de navegação e diário de bordo). O responsável pelo tratamento dos dados é {NAME}, {BUSINESS} (org. nº {ORGNR}), {COUNTRY}. Contato para assuntos de privacidade: {EMAIL}."]),
  ("2. Dados que tratamos", [("ul", [
    "Conta: e-mail e senha (ou login com Google), nome e foto de perfil, número de WhatsApp (opcional).",
    "Contato de emergência (opcional): nome, telefone e número de emergência. O app nunca envia isso sozinho: só monta uma mensagem quando VOCÊ toca em “Pedir ajuda”.",
    "Localização: usada para mostrar sua posição no mapa, tempo, maré, bússola, alarme de fundeio e Homem ao Mar. Só é lida quando você usa essas funções e o app está aberto. Rotas gravadas ficam salvas na sua conta. A posição ao vivo da frota só é enviada se você ligar o compartilhamento e é apagada automaticamente após 24 horas.",
    "Anúncios que você publica: título, preço, descrição, localização e fotos.",
    "Dados do seu barco: diário de bordo, inventário, lembretes de manutenção, favoritos e buscas salvas.",
    "Notificações: um código do aparelho (push token) para avisar sobre buscas salvas.",
    "Denúncias e bloqueios que você fizer.",
    "Não usamos anúncios de terceiros nem rastreamento entre aplicativos."])]),
  ("3. Para que usamos (base legal)", [("ul", [
    "Prestar o serviço que você pediu (execução de contrato): conta, anúncios, diário, frota, alertas.",
    "Com o seu consentimento: localização, contato de emergência, notificações e compartilhamento de posição com a frota. Você pode retirar o consentimento a qualquer momento nas configurações do aparelho ou do app.",
    "Interesse legítimo: segurança, prevenção de abuso e moderação de conteúdo."])]),
  ("4. Com quem compartilhamos", [
    "Seus dados não são vendidos. Usamos prestadores para operar o app:",
    ("ul", [
    "Supabase (hospedagem do banco de dados, login e arquivos) — servidores na UE (Estocolmo, Suécia).",
    "Expo (envio de notificações push).",
    "Anthropic (análise de travessia por IA): enviamos apenas o título, ano, comprimento, preço e texto do anúncio — nunca dados pessoais da sua conta.",
    "Open-Meteo, Kartverket, OpenStreetMap (Nominatim/Overpass) e OpenSeaMap: recebem coordenadas aproximadas para previsão do tempo, maré, nome do local e pontos náuticos.",
    "Apple Mapas / Google Maps (exibição do mapa) e Google (login, se você escolher).",
    "Outros usuários: o que você publica em anúncios é público. Membros da sua frota veem sua posição se você compartilhar."]),
    "Anúncios de outros sites (Finn.no, Blocket, DBA, Tori etc.) aparecem como resumo de fatos (preço, ano, tamanho, local) com link para o anúncio original; não guardamos as fotos nem os textos deles."]),
  ("5. Por quanto tempo guardamos", [("ul", [
    "Dados da conta e do barco: até você excluir a conta.",
    "Posição ao vivo da frota: 24 horas.",
    "Cópias de segurança do provedor podem manter dados excluídos por até cerca de 30 dias antes de serem apagadas.",
    "Denúncias: enquanto forem necessárias para a segurança da comunidade."])]),
  ("6. Seus direitos", [
    "Você pode pedir acesso, correção, exclusão, limitação, portabilidade e oposição, e reclamar à autoridade de proteção de dados do seu país (por exemplo, a Datatilsynet na Noruega ou a ANPD no Brasil).",
    "Para excluir tudo: no app, Perfil → “Excluir minha conta”. Ela apaga a conta, anúncios, diário, rotas, frota e fotos. Para os demais pedidos, escreva para {EMAIL}."]),
  ("7. Crianças", ["O Sextant não é destinado a menores de 16 anos."]),
  ("8. Segurança", ["Usamos conexão criptografada e regras de acesso por usuário no banco de dados. Nenhum sistema é 100% seguro; se ocorrer um incidente que afete você, avisaremos conforme a lei."]),
  ("9. Mudanças", ["Podemos atualizar esta política. A data acima indica a versão atual; mudanças relevantes serão avisadas no app."]),
 ]),
 terms=("Termos de Uso", [
  ("1. Aceite", ["Ao usar o Sextant você concorda com estes termos e com a Política de Privacidade."]),
  ("2. Não é um instrumento de navegação oficial", ["O Sextant é apoio à navegação e ao dia a dia do barco. NÃO substitui cartas náuticas oficiais, instrumentos de bordo, previsão oficial ou bom senso marinheiro. Previsão, maré, bússola, alarmes (fundeio, Homem ao Mar), análise por IA e posição podem falhar ou ser imprecisos. Em emergência no mar use o Canal 16 do VHF e o número de emergência local. O botão de ajuda NÃO aciona a guarda costeira automaticamente."]),
  ("3. Conteúdo de usuários e conduta", [("ul", [
    "Você é responsável pelo que publica e declara ter direito de usar textos e fotos.",
    "Tolerância zero para conteúdo ofensivo, ilegal, golpes, spam, anúncios falsos ou que violem direitos de terceiros.",
    "Você pode denunciar anúncios e bloquear vendedores no app. Analisamos denúncias e podemos remover conteúdo e encerrar contas que violem estes termos."])]),
  ("4. Compra e venda", ["O Sextant apenas conecta pessoas e mostra anúncios. Não somos parte das negociações, não garantimos os anúncios, preços ou a conduta de vendedores. Confira o barco, os documentos e o vendedor antes de pagar."]),
  ("5. Links de afiliados", ["Alguns links para lojas podem gerar comissão ao Sextant, sem custo extra para você. Quando isso ocorrer, será indicado no app."]),
  ("6. Disponibilidade e responsabilidade", ["O app é oferecido “como está”. Na máxima extensão permitida pela lei, não nos responsabilizamos por danos decorrentes do uso ou da indisponibilidade do app. Isso não limita direitos que a lei do consumidor garante e que não podem ser excluídos."]),
  ("7. Lei aplicável", ["Estes termos seguem a lei norueguesa, sem prejuízo dos direitos do consumidor do seu país."]),
  ("8. Contato", ["{NAME} — {BUSINESS} (org. {ORGNR}) — {EMAIL}"]),
 ]))

L["en"] = dict(
 lang="en", label="English", title="Sextant — Privacy & Terms", updated="Last updated",
 privacy=("Privacy Policy", [
  ("1. Who we are", ["Sextant is a nautical app (map of boats, parts and services, navigation tools and a logbook). The data controller is {NAME}, {BUSINESS} (org. no. {ORGNR}), {COUNTRY}. Privacy contact: {EMAIL}."]),
  ("2. Data we process", [("ul", [
    "Account: e-mail and password (or Google sign-in), name and profile photo, WhatsApp number (optional).",
    "Emergency contact (optional): name, phone and emergency number. The app never sends this by itself: it only prepares a message when YOU tap “Ask for help”.",
    "Location: used to show your position on the map, weather, tide, compass, anchor alarm and Man Overboard. It is read only when you use these features and the app is open. Recorded routes are saved to your account. Live fleet position is sent only if you turn sharing on and is deleted automatically after 24 hours.",
    "Listings you publish: title, price, description, location and photos.",
    "Your boat data: logbook, inventory, maintenance reminders, favourites and saved searches.",
    "Notifications: a device token (push token) to alert you about saved searches.",
    "Reports and blocks you make.",
    "We do not use third-party advertising or cross-app tracking."])]),
  ("3. Why we use it (legal basis)", [("ul", [
    "To provide the service you asked for (contract): account, listings, logbook, fleet, alerts.",
    "With your consent: location, emergency contact, notifications and sharing your position with your fleet. You can withdraw consent at any time in device or app settings.",
    "Legitimate interest: security, abuse prevention and content moderation."])]),
  ("4. Who we share it with", [
    "We do not sell your data. We use providers to run the app:",
    ("ul", [
    "Supabase (database, sign-in and file hosting) — servers in the EU (Stockholm, Sweden).",
    "Expo (push notification delivery).",
    "Anthropic (AI crossing analysis): we send only a listing’s title, year, length, price and text — never personal data from your account.",
    "Open-Meteo, Kartverket, OpenStreetMap (Nominatim/Overpass) and OpenSeaMap: receive approximate coordinates for weather, tide, place name and nautical points.",
    "Apple Maps / Google Maps (map display) and Google (sign-in, if you choose it).",
    "Other users: what you publish in listings is public. Fleet members see your position if you share it."]),
    "Listings from other sites (Finn.no, Blocket, DBA, Tori, etc.) appear as a summary of facts (price, year, size, place) with a link to the original; we do not store their photos or texts."]),
  ("5. How long we keep it", [("ul", [
    "Account and boat data: until you delete your account.",
    "Live fleet position: 24 hours.",
    "Provider backups may retain deleted data for up to about 30 days before being erased.",
    "Reports: as long as needed for community safety."])]),
  ("6. Your rights", [
    "You may request access, correction, deletion, restriction, portability and object, and complain to your data protection authority (for example Datatilsynet in Norway).",
    "To delete everything: in the app, Profile → “Delete my account”. It erases your account, listings, logbook, routes, fleet and photos. For other requests write to {EMAIL}."]),
  ("7. Children", ["Sextant is not intended for people under 16."]),
  ("8. Security", ["We use encrypted connections and per-user access rules in the database. No system is 100% secure; if an incident affects you, we will notify you as required by law."]),
  ("9. Changes", ["We may update this policy. The date above shows the current version; significant changes will be announced in the app."]),
 ]),
 terms=("Terms of Use", [
  ("1. Acceptance", ["By using Sextant you agree to these terms and the Privacy Policy."]),
  ("2. Not an official navigation instrument", ["Sextant is an aid for navigation and everyday boat life. It does NOT replace official nautical charts, onboard instruments, official forecasts or good seamanship. Forecast, tide, compass, alarms (anchor, Man Overboard), AI analysis and position can fail or be inaccurate. In an emergency at sea use VHF Channel 16 and the local emergency number. The help button does NOT contact the coast guard automatically."]),
  ("3. User content and conduct", [("ul", [
    "You are responsible for what you publish and confirm you have the right to use the text and photos.",
    "Zero tolerance for offensive or illegal content, scams, spam, fake listings or anything that infringes others’ rights.",
    "You can report listings and block sellers in the app. We review reports and may remove content and close accounts that break these terms."])]),
  ("4. Buying and selling", ["Sextant only connects people and displays listings. We are not a party to any deal and do not guarantee listings, prices or sellers’ conduct. Check the boat, its documents and the seller before you pay."]),
  ("5. Affiliate links", ["Some links to shops may earn Sextant a commission at no extra cost to you. This will be indicated in the app."]),
  ("6. Availability and liability", ["The app is provided “as is”. To the maximum extent permitted by law we are not liable for damages arising from use or unavailability of the app. This does not limit consumer rights that cannot be excluded by law."]),
  ("7. Governing law", ["These terms are governed by Norwegian law, without prejudice to your consumer rights in your country."]),
  ("8. Contact", ["{NAME} — {BUSINESS} (org. {ORGNR}) — {EMAIL}"]),
 ]))

L["no"] = dict(
 lang="nb", label="Norsk", title="Sextant — Personvern og vilkår", updated="Sist oppdatert",
 privacy=("Personvernerklæring", [
  ("1. Hvem vi er", ["Sextant er en nautisk app (kart over båter, deler og tjenester, navigasjonsverktøy og loggbok). Behandlingsansvarlig er {NAME}, {BUSINESS} (org.nr. {ORGNR}), {COUNTRY}. Kontakt for personvern: {EMAIL}."]),
  ("2. Data vi behandler", [("ul", [
    "Konto: e-post og passord (eller Google-innlogging), navn og profilbilde, WhatsApp-nummer (valgfritt).",
    "Nødkontakt (valgfritt): navn, telefon og nødnummer. Appen sender aldri dette av seg selv: den lager bare en melding når DU trykker «Be om hjelp».",
    "Posisjon: brukes til å vise din posisjon på kartet, vær, tidevann, kompass, ankeralarm og Mann over bord. Den leses bare når du bruker disse funksjonene og appen er åpen. Registrerte ruter lagres på kontoen din. Live-posisjon for flåten sendes bare hvis du slår på deling, og slettes automatisk etter 24 timer.",
    "Annonser du publiserer: tittel, pris, beskrivelse, sted og bilder.",
    "Dine båtdata: loggbok, inventar, vedlikeholdspåminnelser, favoritter og lagrede søk.",
    "Varsler: en enhetskode (push-token) for å varsle om lagrede søk.",
    "Rapporter og blokkeringer du gjør.",
    "Vi bruker ikke tredjepartsannonser eller sporing på tvers av apper."])]),
  ("3. Hvorfor vi bruker dem (rettslig grunnlag)", [("ul", [
    "For å levere tjenesten du ba om (avtale): konto, annonser, loggbok, flåte, varsler.",
    "Med ditt samtykke: posisjon, nødkontakt, varsler og deling av posisjon med flåten. Du kan trekke samtykket når som helst i innstillingene.",
    "Berettiget interesse: sikkerhet, forebygging av misbruk og moderering."])]),
  ("4. Hvem vi deler med", [
    "Vi selger ikke dataene dine. Vi bruker leverandører for å drifte appen:",
    ("ul", [
    "Supabase (database, innlogging og filer) — servere i EU (Stockholm, Sverige).",
    "Expo (push-varsler).",
    "Anthropic (KI-analyse av overfart): vi sender kun annonsens tittel, år, lengde, pris og tekst — aldri personopplysninger fra kontoen din.",
    "Open-Meteo, Kartverket, OpenStreetMap (Nominatim/Overpass) og OpenSeaMap: mottar omtrentlige koordinater for vær, tidevann, stedsnavn og nautiske punkter.",
    "Apple Kart / Google Maps (kartvisning) og Google (innlogging, hvis du velger det).",
    "Andre brukere: det du publiserer i annonser er offentlig. Flåtemedlemmer ser posisjonen din hvis du deler den."]),
    "Annonser fra andre nettsteder (Finn.no, Blocket, DBA, Tori osv.) vises som en oppsummering av fakta (pris, år, størrelse, sted) med lenke til originalen; vi lagrer ikke bilder eller tekster derfra."]),
  ("5. Hvor lenge vi lagrer", [("ul", [
    "Konto- og båtdata: til du sletter kontoen.",
    "Live-posisjon for flåten: 24 timer.",
    "Leverandørens sikkerhetskopier kan beholde slettede data i opptil ca. 30 dager før de fjernes.",
    "Rapporter: så lenge det er nødvendig for sikkerheten i fellesskapet."])]),
  ("6. Dine rettigheter", [
    "Du kan be om innsyn, retting, sletting, begrensning, dataportabilitet og protestere, og klage til Datatilsynet.",
    "For å slette alt: i appen, Profil → «Slett kontoen min». Den sletter konto, annonser, loggbok, ruter, flåte og bilder. For andre henvendelser, skriv til {EMAIL}."]),
  ("7. Barn", ["Sextant er ikke ment for personer under 16 år."]),
  ("8. Sikkerhet", ["Vi bruker kryptert tilkobling og tilgangsregler per bruker i databasen. Ingen system er 100 % sikkert; hvis en hendelse rammer deg, varsler vi som loven krever."]),
  ("9. Endringer", ["Vi kan oppdatere denne erklæringen. Datoen over viser gjeldende versjon; vesentlige endringer varsles i appen."]),
 ]),
 terms=("Brukervilkår", [
  ("1. Aksept", ["Ved å bruke Sextant godtar du disse vilkårene og personvernerklæringen."]),
  ("2. Ikke et offisielt navigasjonsinstrument", ["Sextant er et hjelpemiddel for navigasjon og hverdagen om bord. Det erstatter IKKE offisielle sjøkart, instrumenter om bord, offisiell værvarsling eller godt sjømannskap. Værmelding, tidevann, kompass, alarmer (anker, Mann over bord), KI-analyse og posisjon kan svikte eller være unøyaktige. Ved nød på sjøen, bruk VHF kanal 16 og lokalt nødnummer. Hjelp-knappen kontakter IKKE kystvakten automatisk."]),
  ("3. Brukerinnhold og oppførsel", [("ul", [
    "Du er ansvarlig for det du publiserer og bekrefter at du har rett til å bruke tekst og bilder.",
    "Nulltoleranse for støtende eller ulovlig innhold, svindel, spam, falske annonser eller brudd på andres rettigheter.",
    "Du kan rapportere annonser og blokkere selgere i appen. Vi går gjennom rapporter og kan fjerne innhold og stenge kontoer som bryter vilkårene."])]),
  ("4. Kjøp og salg", ["Sextant kobler bare sammen folk og viser annonser. Vi er ikke part i noen avtale og garanterer ikke for annonser, priser eller selgeres oppførsel. Sjekk båten, dokumentene og selgeren før du betaler."]),
  ("5. Affiliate-lenker", ["Enkelte lenker til butikker kan gi Sextant provisjon uten ekstra kostnad for deg. Dette vil framgå i appen."]),
  ("6. Tilgjengelighet og ansvar", ["Appen leveres «som den er». I den grad loven tillater det, er vi ikke ansvarlige for skade som følge av bruk eller utilgjengelighet. Dette begrenser ikke forbrukerrettigheter som ikke kan utelukkes ved lov."]),
  ("7. Gjeldende lov", ["Vilkårene reguleres av norsk rett, uten at det berører dine forbrukerrettigheter i ditt land."]),
  ("8. Kontakt", ["{NAME} — {BUSINESS} (org. {ORGNR}) — {EMAIL}"]),
 ]))

CSS = "body{font-family:-apple-system,system-ui,Segoe UI,sans-serif;max-width:760px;margin:0 auto;padding:24px 16px 64px;line-height:1.6;color:#1a2b3c;background:#fff}h1{color:#1e3d59;font-size:26px}h2{color:#1e3d59;margin-top:40px;border-bottom:2px solid #e2e8f0;padding-bottom:6px}h3{margin-top:24px;font-size:17px}nav a{margin-right:12px}small{color:#64748b}li{margin:6px 0}@media(prefers-color-scheme:dark){body{background:#0f1720;color:#dbe4ee}h1,h2{color:#9cc4e4}h2{border-color:#2c4a68}small{color:#8fa6bd}a{color:#7ab8e8}}"

def render_block(items, cfg):
    out = []
    for it in items:
        if isinstance(it, tuple) and it[0] == "ul":
            out.append("<ul>" + "".join(f"<li>{html.escape(x.format(**cfg))}</li>" for x in it[1]) + "</ul>")
        else:
            out.append(f"<p>{html.escape(it.format(**cfg))}</p>")
    return "\n".join(out)

def render_section(title, sections, cfg, anchor):
    parts = [f'<h2 id="{anchor}">{html.escape(title)}</h2>']
    for h, body in sections:
        parts.append(f"<h3>{html.escape(h)}</h3>")
        parts.append(render_block(body, cfg))
    return "\n".join(parts)

def build():
    nav = " ".join(f'<a href="{c}.html">{L[c]["label"]}</a>' for c in L)
    for code, d in L.items():
        cfg = dict(CONFIG)
        cfg["COUNTRY"] = {"pt": "Noruega", "en": "Norway", "no": "Norge"}[code]
        priv_title, priv = d["privacy"]
        terms_title, terms = d["terms"]
        page = f'''<!doctype html><html lang="{d["lang"]}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(d["title"])}</title><style>{CSS}</style></head><body>
<nav>{nav}</nav>
<h1>{html.escape(d["title"])}</h1>
<small>{d["updated"]}: {cfg["DATE"]}</small>
<p><a href="#privacy">{html.escape(priv_title)}</a> · <a href="#terms">{html.escape(terms_title)}</a></p>
{render_section(priv_title, priv, cfg, "privacy")}
{render_section(terms_title, terms, cfg, "terms")}
</body></html>'''
        open(f"{code}.html", "w", encoding="utf-8").write(page)
    open("index.html", "w", encoding="utf-8").write(
        f'<!doctype html><html><head><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=en.html"><title>Sextant</title></head><body><p><a href="en.html">Sextant</a> — ' +
        " · ".join(f'<a href="{c}.html">{L[c]["label"]}</a>' for c in L) + "</p></body></html>")
    left = [k for k, v in CONFIG.items() if "{{" in v]
    print("gerado. Pendente de preencher:", left or "nada")

if __name__ == "__main__":
    build()
