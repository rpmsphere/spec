Name: naufrago
Summary: A simple RSS/feed reader
Version: 0.4
Release: 5.1
Group: Applications/Internet
License: GPLv3
URL: http://naufrago.sourceforge.net/
Source0: http://sourceforge.net/projects/naufrago/files/%{name}-%{version}.tar.bz2
BuildArch: noarch
Requires: pywebkitgtk
Requires: python-feedparser

%description
Naufrago allows reading news with its images even when it's not afloat, or
what's the same, without being online. This is because there are people, like
the author, that not always has an Internet connection available at a given
time, but wants to be able to read articles/entries/posts with its images.
This is the leit motiv of the application.

%prep
%setup -q -n %{name}

%build

%install
install -d %{buildroot}%{_datadir}/%{name}
cp -a %{name}.py content locale media %{buildroot}%{_datadir}/%{name}
install -Dm644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -d %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
exec python %{name}.py
EOF

%files
%doc LICENSE doc/*
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Jun 09 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuild for Fedora
