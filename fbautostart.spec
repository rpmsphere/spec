Name: fbautostart
Summary: XDG compliant autostarting app for Fluxbox
Version: 2.71828
Release: 1
License: GPL
Group: System/GUI/Other
Source: http://launchpadlibrarian.net/64479893/%{name}-%{version}.tar.gz
URL: https://launchpad.net/fbautostart
Requires: fluxbox

%description
The fbautostart app was designed to have little to no overhead, while still
maintaining the needed functionality of launching applications according to
the XDG spec. This package contains support for GNOME and KDE.

%prep
%setup -q
sed -i '1i #include <unistd.h>' src/fbautostart.cpp

%build
./configure --prefix=/usr
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS ChangeLog COPYRIGHT README.markdown THANKS
%{_bindir}/%{name}
%{_mandir}/man?/%{name}.?.gz

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.71828
- Rebuild for Fedora
