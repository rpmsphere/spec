%undefine _debugsource_packages
Name:			tpfand
Version:		0.94
Release:		11.1
Summary:		ThinkPad Fan Control Daemon
Source:			https://launchpad.net/tp-fan/tpfand/%{version}/+download/tpfand-%{version}.tar.gz
Patch1:			tpfand-makefile.patch
URL:			https://launchpad.net/tp-fan
Group:			Hardware/Mobile
License:		GNU General Public License version 3 (GPL v3)
BuildArch:		noarch
BuildRequires:	python2-devel
BuildRequires:  perl-podlators
Requires:		dbus-python pygobject2

%description
tpfand controls the system fan of ThinkPad notebooks based on specified
temperature profiles. Seperate trigger points can be configured for every
temperature sensor in the notebook.
tpfand is written entirely in Python and licensed under the GNU GPL version 3.

Authors:
--------
    Sebastian Urban <surban84@googlemail.com>

%prep
%setup -q
%patch1
sed -i 's|temperature in.*C|temperature in Celsius|' man/tpfand.pod

%build
%__make

%install
%__rm -rf "$RPM_BUILD_ROOT"
make DESTDIR=$RPM_BUILD_ROOT install PY_SITEDIR="%{python2_sitelib}" MANDIR="%{_mandir}" PREFIX="%{_prefix}"

%__install -d "$RPM_BUILD_ROOT/usr/sbin"
%__ln_s ../../etc/init.d/tpfand "$RPM_BUILD_ROOT/usr/sbin/rctpfand"

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_sbindir}/* %{buildroot}%{python2_sitelib}/tpfand/*.py

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%doc COPYING README
%config(noreplace) /etc/tpfand.conf
%dir %{_sysconfdir}/acpi
%dir %{_sysconfdir}/acpi/resume.d
%config %{_sysconfdir}/acpi/resume.d/91-tpfand-start.sh
%dir %{_sysconfdir}/acpi/suspend.d
%config %{_sysconfdir}/acpi/suspend.d/09-tpfand-stop.sh
%dir %{_sysconfdir}/dbus-1
%dir %{_sysconfdir}/dbus-1/system.d
%config %{_sysconfdir}/dbus-1/system.d/tpfand.conf
/etc/init.d/tpfand
/usr/sbin/rctpfand
%config /etc/modprobe.d/thinkpad_acpi.modprobe
%{python2_sitelib}/tpfand
%{_sbindir}/tpfand
%doc %{_mandir}/man8/tpfand.8*
%{_datadir}/tpfand

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.94
- Rebuilt for Fedora
* Wed Apr 22 2009 Pascal Bleser <pascal.bleser@opensuse.org> 0.94
- new package
