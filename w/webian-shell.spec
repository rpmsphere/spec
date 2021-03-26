Name: 		webian-shell
Version: 	0.1
Release: 	19
Summary: 	A full screen web browser
Group:   	Applications/Internet
License: 	GPL
URL:     	http://webian.org/shell/
Source0:  	https://download.github.com/webianproject-shell-0.1-19-gb2ef9ed.tar.gz
Source1:	%{name}.png
Requires:	chromeless
BuildArch:	noarch

%description
If you find most of the stuff you do on your PC these days happens in a web
browser then you might find that the desktop environment you used to depend
on is now just getting in your way.

The idea of the Webian Shell project is to re-think your computer's interface
as something much simpler which treats web applications as first class citizens
and does away with all the un-necessary clutter.

%prep
%setup -q -n webianproject-shell-b2ef9ed

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a * %{SOURCE1} %{buildroot}%{_datadir}/%{name}

#xdg menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Webian Shell
Comment=A full screen web browser
Exec=%{name}
Icon=%{_datadir}/%{name}/%{name}.png
Terminal=false
Type=Application
StartupNotify=true
Categories=Network;
EOF

#make Excutable
mkdir -p %{buildroot}%{_bindir}
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} << EOF
#!/bin/sh
cd %{_datadir}/%{name}
chromeless index.html
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%attr(755,root,root) %_bindir/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Fri Jun 24 2011 Wei-Lun Chao <bluebat@member.fsf.org> 0.1-19.ossii
- Initial package for OSSII
