-- Agrupa o conteúdo para centralizá-lo na área útil, mantendo o título no topo.
function Pandoc(doc)
  if not FORMAT:match("revealjs") then return doc end
  local saida = pandoc.List()
  local corpo = pandoc.List()
  local em_slide = false
  local function fechar()
    if #corpo > 0 then
      saida:insert(pandoc.Div(corpo, pandoc.Attr("", {"slide-body"})))
      corpo = pandoc.List()
    end
  end
  for _, bloco in ipairs(doc.blocks) do
    if bloco.t == "Header" and bloco.level <= 2 then
      fechar()
      saida:insert(bloco)
      em_slide = bloco.level == 2
    elseif em_slide then
      corpo:insert(bloco)
    else
      saida:insert(bloco)
    end
  end
  fechar()
  doc.blocks = saida
  return doc
end
