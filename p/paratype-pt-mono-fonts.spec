%define _fontdir pt-mono

Name:           paratype-pt-mono-fonts
Version:        1.002OFL
Release:        2.1
Summary:        Monospaced Fonts for Minority Languages of Russia
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            http://www.paratype.com/public/
Source0:        http://www.fontstock.com/public/PTMonoOFL.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
PT Mono was developed for the special needs — for use in forms, tables,
work sheets etc. Equal widths of characters are very helpful in setting
complex documents, with such font you may easily calculate size of entry
fields, column widths in tables and so on. One of the most important
area of use is Web sites of “electronic governments“ where visitors have
to fill different request forms. Currently PT Mono consists of Regular
and Bold styles.

The fonts beside standard Western, Central European and Cyrillic code
pages contain characters of all title languages of Russian Federation
that make them unique and very important tool of the modern digital
communications.

%prep
%setup -q -c
sed -i 's/\r$//g' PTSSM_OFL.txt

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
install -dm 0755 $RPM_BUILD_ROOT%{_datadir}/fonts/%{_fontdir}
install -m 0644 *.ttf $RPM_BUILD_ROOT%{_datadir}/fonts/%{_fontdir}

%files
%defattr(-,root,root,-)
%doc PTSSM_OFL.txt
%{_datadir}/fonts/%{_fontdir}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Tue Aug 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.002OFL
- Rebuild for Fedora
* Thu Mar 29 2012 lazy.kent@opensuse.org
- Update to 1.002OFL.
  * Added Bold style.
* Sat Jan 28 2012 lazy.kent@opensuse.org
- Update to 1.001OFL.
  * Corrected "г", "ю", "l" and some characters with accents.
  * Ligatures moved from "liga" to "dlig".
* Sat Jan  7 2012 lazy.kent@opensuse.org
- Initial package created - 1.000OFL
