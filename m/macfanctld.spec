%undefine _debugsource_packages

Name:           macfanctld
BuildRequires:  gcc make
License:        GPL v2
Group:          System/Kernel
Summary:        Apple fan control daemon
Version:        0.3
Release:        18.1
Source:         %{name}-%{version}.tar.bz2
Source1:        macfanctl.conf
Source2:        macfanctld.1
Source3:        macfanctld
Patch:          Makefile.patch

%description -n macfanctld
macfanctld is a daemon that reads temperature sensors and adjust the fan(s)
speed on MacBook's. macfanctld is configurable and logs temp and fan data to
a file. macfanctld uses three sources to determine the fan speeed: 1) average
temperature from all sensors, 2) sensor TC0P [CPU 0 Proximity Temp and 3] and
sensor TG0P [GPU 0 Proximity Temp]. Each source's impact on fan speed can be
individually adjusted to fine tune working temperature on different MacBooks.

Important: macfanctld depends on applesmc.

%prep
%setup -q -n %{name}
%patch -p0
%build
make 

%install
mkdir -p $RPM_BUILD_ROOT/etc
mkdir -p $RPM_BUILD_ROOT/etc/init.d
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/sbin
install -m 0644 %{S:1} $RPM_BUILD_ROOT/etc/
install -m 0644 %{S:2} $RPM_BUILD_ROOT/usr/share/man/man1/
install -m 0755 macfanctld $RPM_BUILD_ROOT/usr/sbin/
install -m 0755 %{S:3} $RPM_BUILD_ROOT/etc/init.d/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%config %{_sysconfdir}/macfanctl.conf
%{_sysconfdir}/init.d/macfanctld
%{_datadir}/man/man1/macfanctld.1.gz
%{_sbindir}/macfanctld

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuilt for Fedora
* Mon Oct 18 2010 alinm.elena@gmail.com
- initial commit
