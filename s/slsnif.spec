Name:           slsnif
Version:        0.4.4
Release:        2.1
Summary:        Serial line sniffer

Group:          Applications/Communications
License:        GPLv2+
URL:            https://slsnif.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

%description
Serial line sniffer (slsnif). slsnif is a serial port logging utility. It
listens to the specified serial port and logs all data going through this
port in both directions.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%doc AUTHORS ChangeLog COPYING NEWS README TODO slsnifrc-example
%{_mandir}/man*/%{name}.1*
%{_bindir}/%{name}

%changelog
* Thu Feb 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.4
- Rebuilt for Fedora

* Thu Jan 15 2009 Fabian Affolter <fabian@bernewireless.net> - 0.4.4-1
- Initial package for Fedora
