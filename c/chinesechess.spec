Name:           chinesechess
Version:        1.0
Release:        3.1
Summary:        Chinese Chess
License:        freeware
URL:            http://www.codefans.net
Source0:        Chess-%{version}.zip
BuildRequires:  java-devel-openjdk lua
Requires:       jre
BuildArch:      noarch

%description
Chinese Chess board written in Java.

%prep
%setup -q -c

%build
javac -encoding UTF-8 Chess.java

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a *.class image $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/sh
cd %{_datadir}/%{name}
java Chess
EOF

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Oct 10 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
