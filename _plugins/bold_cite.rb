module Jekyll
    class RenderBoldCiteTagBlock < Liquid::Block
      def render(context)
        raw_text = super
        context.registers[:site].collections["people"].docs.each do |person|
            person_names = [person.data["name"]]
            person_names += person.data["pub_names"]
            person_names.each do |person_name|
                new_text = raw_text.gsub(%r{#{person_name}}) do |match|
                    "<b>#{match}</b>"
                end
                if raw_text != new_text
                    raw_text = new_text
                    break
                end
            end
        end

        raw_text
      end

    end
end

Liquid::Template.register_tag('render_bold_cite', Jekyll::RenderBoldCiteTagBlock)
