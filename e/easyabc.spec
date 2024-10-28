Name:      easyabc
Version:   1.3.8.6
Release:   1
Summary:   An open source ABC editor for Windows, OSX and Linux
License:   GPL
URL:       https://easyabc.sourceforge.net/
Group:     Applications/Multimedia
Requires:  python3-wxpython4-media, python3-pygame, python3-pyparsing
Requires:  abcm2ps, abcMIDI, nwc2xml
BuildArch: noarch
Source:    https://sourceforge.net/projects/easyabc/files/EasyABC/%{version}/EasyABC-%{version}-source.zip

%description
EasyABC is an open source ABC editor for Windows, OSX and Linux. It
uses abcm2ps and abc2midi, and it has a rich feature list. Most
notably, it can import MusicXML files and export tunes in SVG format.

%prep
#setup -q -n EasyABC.%{version}
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -R * $RPM_BUILD_ROOT%{_datadir}/%{name}
echo "#!/bin/sh" > easyabc
echo "python3 /usr/share/easyabc/easy_abc.py" >> easyabc
install -Dm755 easyabc $RPM_BUILD_ROOT%{_bindir}/%{name}
#ln -s /usr/bin/abcm2ps $RPM_BUILD_ROOT%{_datadir}/%{name}/bin/abcm2ps
#ln -s /usr/bin/abc2abc $RPM_BUILD_ROOT%{_datadir}/%{name}/bin/abc2abc
#ln -s /usr/bin/abc2midi $RPM_BUILD_ROOT%{_datadir}/%{name}/bin/abc2midi
#ln -s /usr/bin/nwc2xml $RPM_BUILD_ROOT%{_datadir}/%{name}/bin/nwc2xml

%files
%doc CHANGES LICENSE *.txt
%{_datadir}/%{name}
%{_bindir}/easyabc

%changelog
* Sun Mar 20 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.8.6
- Rebuilt for Fedora
* Wed May 22 2013 Guido Gonzato <guido.gonzato at gmail.com>
- This is a generic rpm, buildable on Ubuntu
