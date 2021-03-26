Name: WhyCantIConnect
Summary: Why Can't I Connect?
Version: 1.12.4
Release: 1
Group: Applications/System Applications/Network
License: GPL
URL: https://www.whycanticonnect.com/
Source0: http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}.tar.gz
BuildRequires: desktop-file-utils
BuildRequires: wxGTK3-devel
BuildRequires: openssl-devel

%description
"Why Can't I Connect" makes it easier to resolve
TCP/IP connection errors.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
#{_datadir}/doc/%{name}
%{_datadir}/pixmaps/%{name}Icon.png

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.12.4
- Rebuild for Fedora
