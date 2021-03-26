%define _name SourceSansPro
%define	fontdir	%{_datadir}/fonts/source-sans

Name:           source-sans-fonts
Version:        1.038
Release:        4.1
Summary:        A set of OpenType fonts designed for user interfaces
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            http://sourceforge.net/projects/sourcesans.adobe/
Source:         %{_name}_FontsOnly-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Source Sans is a set of OpenType fonts that have been designed to work well
in user interface (UI) environments, as well as in text setting for screen
and print.

%prep
%setup -q -n %{_name}_FontsOnly-%{version}
# Fix line endings
sed -i 's/\r$//g' LICENSE.txt

%build

%install
install -d %{buildroot}%{fontdir}
install TTF/*.ttf %{buildroot}%{fontdir}

%files
%defattr(-,root,root)
%doc LICENSE.txt *.html
%{fontdir}/*

%changelog
* Sun Dec 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.038
- Rebuild for Fedora
* Sat Oct 27 2012 toms@opensuse.org
- Update to version 1.038 (2012/09/12):
  * Updates the metrics of Majuscule letters in lighter weights.
  * Updates fonts to add small capitals and superior capital letters
  to upright styles.
  * Adds the following characters for transliteration: Blinebelow,
  blinebelow, Klinebelow klinebelow, Emacronacute, emacronacute,
  Omacronacute, omacronacute, primemod
  * Adds the following punctuation characters: bardbl, iterrobang,
  ceilingleft, ceilingright, floorleft floorright, bracketleftwhite,
  bracketrightwhite, brackhalftopleft, brackhalftopright, brackhalfbotleft,
  brackhalfbotright
  * Adds dotted zero and slashed zero.
* Fri Sep 28 2012 toms@opensuse.org
- Added Obsoletes and Provides
* Fri Sep 28 2012 toms@opensuse.org
- Renamed from SourceSansPro package, fixed .changes and .spec file
* Tue Sep 25 2012 toms@opensuse.org
- Spec: Use %%{_ttfontsdir} macro instead of %%{_datadir}
* Sun Sep 23 2012 toms@opensuse.org
- Updated to 1.0.36 release
  Updates fonts to fix bug in TTF versions in which the GDEF table
  was not included.
- 1.0.35 release:
  Updates the fitting for 'u' and its related glyphs. Updates the
  kerning in the upright fonts.
* Mon Aug 27 2012 toms@opensuse.org
- amend spec file to reflect new font packaging scheme
  (see openFATE#313536)
* Wed Aug 22 2012 toms@opensuse.org
- Included SourceSansProReadMe.html file into %%doc path
  (contains changelog)
* Tue Aug 21 2012 toms@opensuse.org
- Update to 1.0.34 release
- SPEC file changes:
  . Fix line endings for LICENSE.txt
  . Adapted to new structure in archive
  . Installed both, OTF and TTF files
* Sat Aug  4 2012 dimstar@opensuse.org
- Update to latest 1.033 release
  + No real change, except that we have proper version numbers.
* Fri Aug  3 2012 dimstar@opensuse.org
- Initial package, version from 2012-07-31.
