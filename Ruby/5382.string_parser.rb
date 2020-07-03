def entity_parser(text)
    text.gsub! '&amp;', '&'
    text.gsub! '&apos;', "'"
    text.gsub! '&quot;', '"'
    text.gsub! '&gt;', '>'
    text.gsub! '&lt;', '<'
    text.gsub! '&frasl;', '/'
end

text = "&amp; is an HTML entity but &ambassador; is not."
p entity_parser(text)