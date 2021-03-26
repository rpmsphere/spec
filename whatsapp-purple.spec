%global debug_package %{nil}

Name: whatsapp-purple
Summary: WhatsApp protocol implementation for libpurple (Pidgin)
Version: 0.6
Release: 4.4
Group: System Environment/Libraries
License: GPLv2
URL: https://github.com/davidgfnet/whatsapp-purple/
Source0: %{name}-%{version}.tar.gz
BuildRequires: libpurple-devel

%description
This is a WhatsApp plugin for Pidgin and libpurple messengers. It connects
to the WhatsApp servers using the password (which needs to be retrieved
separately). Only one client can connect at a time (including your phone).

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
%make_install

%files
%doc README.md
%{_libdir}/purple-2/libwhatsapp.so
%{_datadir}/pixmaps/pidgin/protocols/*/whatsapp.png

%changelog
* Mon Jan 19 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuild for Fedora
