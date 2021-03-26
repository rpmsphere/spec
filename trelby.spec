Name:		trelby
Version:	2.2
Release:	3.1
Summary:	Movie screenplay writing software
License:	GPL
Group:		Applications/Editors
Source0:	http://www.trelby.org/files/release/%{version}/%{name}-%{version}.tar.gz
URL:		http://www.trelby.org/
BuildArch:	noarch
Requires:	python2-wxpython, python-crypto, python-lxml

%description
A simple, powerful, full-featured, multi-platform, program for writing movie
screenplays. Free alternative to Final Draft / Movie Magic Screenwriter.

%prep
%setup -q
sed -i 's|/opt|/usr/share|' trelby/trelby.desktop trelby/src/misc.py

%build

%install
rm -rf $RPM_BUILD_ROOT
install -Dm644 trelby/trelby.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
mkdir -p $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_datadir}
cp -a %{name} $RPM_BUILD_ROOT%{_datadir}
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} << EOF
#!/bin/sh
cd %{_datadir}/%{name}/src
python2 %{name}.py
EOF

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/src/%{name}.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Fri Nov 01 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2
- Rebuild for Fedora
