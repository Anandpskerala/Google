AUTHOR = 'Marco Aceti'
AUTHOR_HREF = 'https://www.github.com/MarcoBuster/'
LANGUAGE = 'English'  # Must be in english
LANGUAGE_CODE = 'en'  # Must respect this: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

# TODO: Reorder strings

STRINGS = [
    {
        'start': '<b>Welcome in the bot!</b>\nYou are using <b>english translation</b>.',
        'sign_in': '👤 <b>Sign in with Google</b>'
                   '\nSign in with Google for use this bot',
        'sign_in_button': '👤 Sign in with Google',
        'back_button': '🔙 Return back',
        'news_button': '📰 News',
        'settings_button': '⚙ Settings',
        'settings': 'What setting do you want to change?',
        'trends_button': '📊 Trends',
        'trends': '🔍 Insert an <b>argument</b> that you would to view the 📊  <b>stats</b>',
        'trends_not_found': '❌ <b>No results</b>\nTry to search more general things',
        'generating_graph': '🔄 <b>I\'m generating the graph...</b>',
        'generated_graph': '✅ <b>Graph generated successfully.</b>',
        'calendar_button': '📅 Calendar',
        'setlan_button': '⚙ Change language',
        'setlan': '<b>Select new language</b>',
        # -- Calendar plugin strings --
        # Events list
        'header': '📅 <b>All events in your calendar</b>',
        'event_by': 'created by',
        'your_self': 'yourself',
        'no_title': 'No title',
        'start_event_time': 'from hour {hour} of day {date}',
        'end_event_time': 'to hour {hour} of day {date}',
        'all_day_time': 'all day {day}',
        'no_events': '📅 <b>There aren\'t events on your calendar</b>',
        # Create event
        'create_event_header': '📅  <b>Event creation</b>\n',
        'create_event_notext_error': '❌ The message <b>doesn\'t contain any text.</b>\nPlease, <b>try again.</b>',
        'create_event_timeformatting_error': '❌ <b>Error in the time\'s format</b>'
                                             '\nThe correct format is: <code>hh:mm dd/mm/yyy</code>'
                                             ' - <code>hh:mm dd/mm/yyyy</code>',
        'create_event_first_step': '1️⃣ <i>Insert the event\'s name</i>'
                                   '\nIf you want to add a <b>description</b>, add a dot'
                                   ' <code>.</code> at the end of the name,'
                                   ' followed by the description, for example:'
                                   '\n<code>Dinner with Clara. Remember to buy chocolates!</code>',
        'create_event_second_step': '2️⃣ <i>Enter the starting and ending time of your event</i>'
                                    '\nWrite the <b>starting</b> and <b>ending dates</b> of your event'
                                    ' in this format: <code>hh:mm dd/mm/yyyy</code>.'
                                    ' Put a dash <code>-</code> between the two, for example:'
                                    '\n<code>12:30 22/02/2017 - 13:10 22/02/2017</code>',
        'create_event_completed': '🆗 <i>Done!</i>'
                                  '\n<b>Event\'s name</b>: {name}'
                                  '{description}'
                                  '\n<a href="{url}">Click here to view the event on Google Calendar.</a>',
        'create_event_completed_description': '\n<b>Description</b>: {description}',
        # Update event  TODO: Find a traslator and traslate this
        'update_event': 'edit',
        'update_event_header': '📅  <b>Modifica di un evento</b>\n',
        'update_event_first_step': '1️⃣ <i>Inserisci il nuovo nome dell\'evento</i>'
                                   '\nSe vuoi aggiungere una <b>descrizione</b>, aggiungi alla fine'
                                   ' un punto <code>.</code>'
                                   ' seguito dalla tua descrizione, per esempio:'
                                   '\n<code>Cena con Clara. Ricordati di comprare i cioccolatini!</code>',
        'update_event_second_step': '2️⃣ <i>Inserisci la nuova ora di inizio e di fine del tuo evento</i>'
                                    '\nScrivi la <b>data di inizio</b> e <b>di fine</b> del tuo evento'
                                    ' in questo formato: <code>ora:minuto giorno/mese/anno</code>,'
                                    ' mettendoci un trattino <code>-</code> in mezzo, per esempio:'
                                    '\n<code>12:30 22/02/2017 - 13:10 22/02/2017</code>',
        'update_event_completed': '🆗 <i>Fatto!</i>'
                                  '\n<b>Nome dell\'evento</b>: {name}'
                                  '{description}'
                                  '\n<a href="{url}">Clicca qui per visualizzare l\'evento su Calendari Google</a>',
        'update_event_completed_description': '\n<b>Descrizione</b>: {description}',
        # -- Buttons --
        # Controls
        'first_page': '⏪ First page',
        'next_page': '▶️ Next page',
        # Calendar
        'add_event_button': '➕ Add an event',
        'edit_event_button': '✍️ Modifica',
        'delete_event_button': '🗑 Elimina',
        'update_event_same': '🙈 Lascia così'
    }
]


def get(str_code):
    """Do not edit below, please"""
    for string in STRINGS:
        for key in string:
            if key == str_code:
                return string[key]

        return (
            'Error in translation:'
            '\nAuthor: {a} ({h})'
            '\nLanguage: {l} ({c})'
            '\nRequested string: {r}'.format(a=AUTHOR, h=AUTHOR_HREF, l=LANGUAGE, c=LANGUAGE_CODE, r=str_code)
        )
