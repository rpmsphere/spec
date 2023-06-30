Name:           lwtt 
Summary:        A very simple time-tracking program
Version:        1.2.0
Release:        17.1
Group:          Productivity 
License:        GPL
URL:            https://lwtt.aiken.net
Requires:       jre
BuildRequires:  unzip
BuildRequires:  java-devel lua
BuildRequires:  ant 
Source0:        %{name}-%{version}-src-ext.tar.bz2
Source1:	%{name}.desktop
Source2:        %{name}.svg
Source3:        %{name}.png
BuildArch:      noarch

%description
Lightweight Time Tracker (LWTT) is written in Java (version 6). 
It provides independent real-time tracking of multiple tasks such as
programming, presentations, lectures etc.) including very simple price
calculation. LWTT's data are saved to a XML file under the home directory.

Author(s):
------------
    Lukas Jelinek   <lukas@aiken.cz>

%prep
%setup -q -c

%build
make

%install
# Don't do bytecode version check
#export NO_BRP_CHECK_BYTECODE_VERSION=true

%__install -d -m 755 %{buildroot}%{_datadir}/%{name}
%__install -m 755 *.jar %{buildroot}%{_datadir}/%{name}/

# startscript
cat > %{name} << EOF
#!/bin/sh
java -jar %{_datadir}/%{name}/%{name}.jar
EOF

%__install -d -m 755 %{buildroot}%{_bindir}
%__install -m 755 %{name} %{buildroot}%{_bindir}/

# Icon
%__install -D -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.svg
%__install -D -p -m 644 %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/%{name}.png

# Desktop menu entry
%__install -d -m 755 %{buildroot}%{_datadir}/applications
%__install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
%__rm -rf %{buildroot}

%files
%{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/%{name}.svg
%doc COPYING

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.0
- Rebuilt for Fedora
* Mon Nov 24 2008 lumnis@email.de
- java bytecode check disabled (spec-file)
* Wed Oct  1 2008 lumnis@email.de
- added icons
* Wed Sep 17 2008 lumnis@email.de
- initial package lwtt v1.2.0
