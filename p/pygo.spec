Name: pygo
Summary: A Python/Tk application for studying and playing the ancient game of Go
Version: 0.10.1
Release: 3.1
Group: Amusements/Games
License: GPLv2
URL: http://pygo.sourceforge.net/
Source0: http://prdownloads.sourceforge.net/pygo/%{name}-%{version}.tgz
BuildArch: noarch

%description
There are lots more features planned but the current release is suitable for
studying games in SGF format as well as playing local human versus human games
in the absence of a board.

%prep
%setup -q

%build
cat > %{name} <<EOF
#!/bin/sh
cd %{_datadir}/%{name}
exec python %{name}.py
EOF

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}
cp -a * %{buildroot}%{_datadir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Thu Jan 02 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.10.1
- Rebuilt for Fedora
