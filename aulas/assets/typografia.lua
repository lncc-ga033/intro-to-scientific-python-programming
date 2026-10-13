-- Impede que a pontuação automática dos metadados troque "--" por outro sinal.
local function hifens(el)
  el.text = el.text:gsub(utf8.char(0x2013), "--"):gsub(utf8.char(0x2014), "--")
  return el
end

function Meta(meta)
  for _, campo in ipairs({"title", "subtitle", "pagetitle"}) do
    if meta[campo] and meta[campo].walk then
      meta[campo] = meta[campo]:walk({Str = hifens})
    end
  end
  return meta
end
