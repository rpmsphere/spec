%define _fontdir theano

Name:           theano-fonts
Version:        2.0
Release:        5.1
License:        OFL-1.1
Summary:        Theano Classical Fonts
URL:            https://www.thessalonica.org.ru/en/theano.html
Group:          System/X11/Fonts
Source0:        https://thessalonica.org.ru/downloads/theano-%{version}.otf.zip
Source1:        https://thessalonica.org.ru/downloads/theano-%{version}.ttf.zip
Source2:        https://www.thessalonica.org.ru/downloads/theano-specimen.pdf
BuildArch:      noarch

%description
Theano Classical Fonts include three fonts listed below. Each font is
currently available just in one weight/shape (regular) and contains
Latin, Greek and Cyrillic letters.

Theano Didot.
A classicist face, with both its Roman and Greek parts implemented in
Didot style. Unlike Old Standard, this font is designed from French
sources.

Theano Modern.
A font with Greek letters designed in the Porsonic style. Unlike most
modern implementation, it is based on Figgins Pica No. 3 / Small Pica
No. 2 — probably the most successful and once the most popular Greek
face of a Porsonic origin — rather than on later Monotype's design.
The accompanying Latin font is implemented in the Modern style and
modelled after English Modern faces of later 19th century, often used
alonglide with Porsonic Greek types.

Theano Old Style.
A modernized "Old Style" Greek font with a large number of historic
ligatures and alternate forms, modelled after some early 19th century
types designed by Figgins' type foundry. It is accompanied by a Latin
face based on some "Old Style" Roman fonts of the late 19th and early
20th century.

%package otf
Summary:        Theano Classical Fonts (OpenType Format)
Group:          System/X11/Fonts
Provides:       locale(el;ru)

%description otf
Theano Classical Fonts include three fonts listed below. Each font is
currently available just in one weight/shape (regular) and contains
Latin, Greek and Cyrillic letters.

Theano Didot.
A classicist face, with both its Roman and Greek parts implemented in
Didot style. Unlike Old Standard, this font is designed from French
sources.

Theano Modern.
A font with Greek letters designed in the Porsonic style. Unlike most
modern implementation, it is based on Figgins Pica No. 3 / Small Pica
No. 2 — probably the most successful and once the most popular Greek
face of a Porsonic origin — rather than on later Monotype's design.
The accompanying Latin font is implemented in the Modern style and
modelled after English Modern faces of later 19th century, often used
alonglide with Porsonic Greek types.

Theano Old Style.
A modernized "Old Style" Greek font with a large number of historic
ligatures and alternate forms, modelled after some early 19th century
types designed by Figgins' type foundry. It is accompanied by a Latin
face based on some "Old Style" Roman fonts of the late 19th and early
20th century.

This package contains fonts in OpenType format.

%package ttf
Summary:        Theano Classical Fonts (TrueType Format)
Group:          System/X11/Fonts

%description ttf
Theano Classical Fonts include three fonts listed below. Each font is
currently available just in one weight/shape (regular) and contains
Latin, Greek and Cyrillic letters.

Theano Didot.
A classicist face, with both its Roman and Greek parts implemented in
Didot style. Unlike Old Standard, this font is designed from French
sources.

Theano Modern.
A font with Greek letters designed in the Porsonic style. Unlike most
modern implementation, it is based on Figgins Pica No. 3 / Small Pica
No. 2 — probably the most successful and once the most popular Greek
face of a Porsonic origin — rather than on later Monotype's design.
The accompanying Latin font is implemented in the Modern style and
modelled after English Modern faces of later 19th century, often used
alonglide with Porsonic Greek types.

Theano Old Style.
A modernized "Old Style" Greek font with a large number of historic
ligatures and alternate forms, modelled after some early 19th century
types designed by Figgins' type foundry. It is accompanied by a Latin
face based on some "Old Style" Roman fonts of the late 19th and early
20th century.

This package contains fonts in TrueType format.

%prep
%setup -cqn %{name}-%{version}
unzip -oq %{SOURCE1}
cp %{SOURCE2} .
sed -i 's/\r$//g' OFL-FAQ.txt

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
install -dm 0755 $RPM_BUILD_ROOT%{_datadir}/fonts/%{_fontdir}
install -m 0644 *.otf $RPM_BUILD_ROOT%{_datadir}/fonts/%{_fontdir}
install -m 0644 *.ttf $RPM_BUILD_ROOT%{_datadir}/fonts/%{_fontdir}

%files otf
%doc FONTLOG.txt OFL.txt OFL-FAQ.txt theano-specimen.pdf
%{_datadir}/fonts/%{_fontdir}/*.otf

%files ttf
%doc FONTLOG.txt OFL.txt OFL-FAQ.txt theano-specimen.pdf
%{_datadir}/fonts/%{_fontdir}/*.ttf

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Tue Aug 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuilt for Fedora
* Thu Nov 10 2011 lazy.kent@opensuse.org
- Only otf package provides locale (we don't need both).
- Clean up spec.
* Wed Aug 10 2011 lazy.kent@opensuse.org
- Fixed provided locales
* Thu Jul  7 2011 lazy.kent@opensuse.org
- Provides locale el, ru
* Wed Jun 15 2011 lazy.kent@opensuse.org
- Initial package created - 2.0
