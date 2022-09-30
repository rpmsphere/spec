%undefine _debugsource_packages

Name: code-browser
Summary: A folding text editor
Version: 8.0
Release: 1
Group: Applications/Editors
License: GPLv2
URL: http://tibleiz.net/code-browser/
Source0: http://tibleiz.net/download/%{name}-%{version}-src.tar.gz
Source1: %{name}.mk
Source2: missing-headers.zip
BuildRequires: copper
BuildRequires: gtk3-devel
BuildRequires: libX11-devel

%description
Code Browser is a folding and outlining editor. It is a lightweight but powerful
tool for structuring and browsing source code using folders and links. It is
especially designed to keep a good overview of the code of a large project.

%prep
%setup -q
cp %{SOURCE1} Makefile
unzip %{SOURCE2} -d res
sed -i 's|/usr/include/x86_64-linux-gnu|/usr/include|' libs/copper-ui/Makefile

%build
make with-local-libs

%install
%make_install

%files
%doc *.txt
%{_bindir}/%{name}
%{_datadir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
* Sun Sep 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 8.0
- Rebuilt for Fedora
