Summary: Extra language-spec files of gtksourceview3
Name: gtksourceview3-langs-extra
Version: 2021.01
Release: 1
License: Open Source
Group: Development
Source0: %{name}.zip
BuildArch: noarch
Requires: gtksourceview3

%description
Including extra language-spec files for syntax highlighting of GtkSourceView 3:
http://www.mihr.net/comp/lang/basic/basic.lang.tar.gz#/basic.lang
https://github.com/WEP11/gtksourceview-languages/raw/master/grads.lang
https://github.com/moonsdad/GTKSourceView_LanguageSpecs/raw/master/icon.lang
https://github.com/moonsdad/GTKSourceView_LanguageSpecs/raw/master/kpl.lang
https://github.com/gerryd/gtksourceview-langspec-twig/raw/master/twig.lang
https://github.com/vlastavesely/gtksourceview-langs/raw/master/lang/neon.lang
https://github.com/luc-chante/plantuml-lang/raw/master/plantuml.lang
https://github.com/alinarezrangel/gtksourceview-language-pseudod/raw/master/pseudod.lang
https://github.com/mjziebarth/jass.lang/raw/master/jass.lang
https://github.com/dvberkel/GtkSourceView-PostScript-language-definition/raw/master/language-specs/postscript.lang
https://github.com/austinmarton/mib-lang-def/raw/master/mib.lang
https://github.com/dvberkel/GtkSourceView-MAGMA-language-definition/raw/master/language-specs/magma.lang
https://github.com/AndrewJamesTurner/openSCAD-lang-file/raw/master/scad.lang
https://github.com/skpdvdd/chuck.lang/raw/master/chuck.lang
https://github.com/CriticalBlue/smali-syntax-highlighter/raw/master/smali.lang
https://github.com/mitko/turtle_gedit/raw/master/n3.lang
https://github.com/thomasysliu/Gedit-SPICE-syntax-highlighting/raw/master/spice.lang
https://github.com/programaker/gedit-syntax-highlight/raw/master/ioke.lang
https://github.com/programaker/gedit-syntax-highlight/raw/master/smalltalk.lang
https://github.com/r10s/gtksourceview-abc/raw/master/abc.lang
https://github.com/m007/cypher.lang/raw/master/cypher.lang
https://github.com/Hibou57/ats2-gtksourceview-language-support/raw/master/ats.lang
https://github.com/JakubVanek/ev3sources-asm/raw/master/logo.lang
https://gist.github.com/LiteTabs/6074753/raw/ee7f797be731fb1bb3587a0ecf769153ebb3578f/gistfile1.xml#lisp.lang
http://users.telenet.be/d09/sharel/usr/share/gtksourceview-3.0/asciidoc.lang
https://github.com/SteffenBauer/elixir-gtksourceview/raw/master/elixir.lang
http://conky.pitstop.free.fr/wiki/images/Conky.lang_17_Jun_2013.tar.gz#/conky.lang
https://www.ncl.ucar.edu/Applications/Files/ncl_gedit_xml.tgz#/ncl_gedit_xml/ncl.lang
https://github.com/scottgrizzard/maple.lang/raw/master/maple.lang
https://github.com/Lucki/gtksourceview3-lolcode/raw/master/lolcode.lang
https://github.com/bartwe/pluk-gtksourceview/raw/master/pluk.lang
https://github.com/ekiwi/firrtl-gtksourceview/raw/master/firrtl.lang
https://github.com/wesinator/GtkSourceView-YARA/raw/master/yara.lang
https://github.com/jorgeramirez/sl-highlight/raw/master/sl.lang
http://lilypond.1069038.n5.nabble.com/attachment/205176/0/lilypond.lang
https://github.com/StefanSalewski/NEd/raw/master/nim.lang
https://github.com/mattfenwick/gedit-clojure/raw/master/clojure.lang
https://github.com/Freddy1404/ponylang_gtksourceview/raw/master/pony.lang
https://spivey.oriel.ox.ac.uk/wiki/files/ip/oberon.lang
http://nitlanguage.org/nit.git/blob_plain/HEAD:/misc/gtksourceview/nit.lang
http://users.telenet.be/d09/sharel/usr/share/gtksourceview-3.0/rexx.lang

%prep
%setup -q -c

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/gtksourceview-3.0/language-specs
install -m644 *.lang %{buildroot}%{_datadir}/gtksourceview-3.0/language-specs

%clean 
rm -rf %{buildroot}

%files
%{_datadir}/gtksourceview-3.0/language-specs/*.lang

%changelog
* Fri Jan 15 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2021.01
- Rebuilt for Fedora
