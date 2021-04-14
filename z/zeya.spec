Name:           zeya
Version:        0.5
Release:        1
Summary:	A web music server
Group:          Applications/Multimedia
License:	GPLv3
URL:            http://web.psung.name/zeya/
Source0:        %{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	python-tag, mpg321, flac, vorbis-tools

%description
Zeya is a streaming music server that brings your music to any computer
with a web browser. It reads your music library, lets you browse your
files, and streams them on demand.

The client runs entirely in the browser using the HTML5 draft standard
technologies (no plugins or external players are needed).

This package includes the Zeya HTTP server and a small command-line client
for machines where no HTML5-capable browser is available.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
./%{name}.py --path=\$HOME/Music
EOF

#Desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Zeya
Comment=A web music server
Exec=%{name}
Terminal=false
Type=Application
Icon=/usr/share/zeya/resources/favicon.png
Categories=Application;AudioVideo;
EOF

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5
- Rebuilt for Fedora
