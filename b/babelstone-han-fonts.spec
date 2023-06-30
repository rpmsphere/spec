%global _ttfontsdir %{_datadir}/fonts/babelstone

Name:           babelstone-han-fonts
Version:        13.0.0
Release:        1
Summary:        Font for Han Script
License:        APL
Group:          System/X11/Fonts
URL:            https://www.babelstone.co.uk/Fonts/
Source0:        https://babelstone.co.uk/Fonts/BabelStoneHan.zip
Source1:        %name.LICENSE
BuildArch:      noarch

%description
BabelStone Han is a dual-width Unicode Han font in Song/Ming style 
with G-source glyphs used in the People's Republic of China.

%prep
%setup -q -c

%build
cp -a %{SOURCE1} LICENSE

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}

%files
%doc LICENSE
%{_ttfontsdir}

%changelog
* Tue Nov 26 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 13.0.0
- Rebuilt for Fedora
* Sat Dec 12 2015 p.drouand@gmail.com
- Update to version 8.0.2
  * More glyph corrections
  * 5 additional CJK-B characters.
- Changes from version 8.0.1
  * 269 CJK-A characters
  * 428 CJK-B characters
  * 97 CJK-C characters
  * 209 CJK-E characters
  * 1,671 PUA characters added from BabelStone Han PUA
  * Various glyph corrections.
* Tue Oct 27 2015 p.drouand@gmail.com
- Update to version 8.0.0
  * 9 characters added to the end of the main CJK block
  * 115 CJK-A characters
  * 363 CJK-B characters
  * 30 CJK-C characters
  * 1,125 CJK-E characters
  * 194 PUA characters removed.
* Thu Oct 17 2013 pgajdos@suse.com
- initial version 1.11
