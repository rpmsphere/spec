Name: lterm
Summary: Free terminal and multiprotocol client
Version: 1.5.0
Release: 1
Group: Applications/Communications
License: GPL2+
URL: http://lterm.sourceforge.net/
Source0: http://sourceforge.net/projects/lterm/files/%{name}-%{version}.tar.gz
BuildRequires: vte291-devel, libssh-devel

%description
lterm is a vte-based terminal emulator for GNU/Linux systems. It is mainly
used as SSH/Telnet client but can be very easily configured to use any other
protocol. Furthermore it can be a usual terminal on local host.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc README AUTHORS ChangeLog COPYING NEWS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/*
%exclude %{_datadir}/mime/*

%changelog
* Tue Aug 15 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.0
- Rebuilt for Fedora
