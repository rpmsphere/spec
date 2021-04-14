Summary:   SUMU theme for GDM
Name:      sumu-gdm-theme
Version:   3.0.7
Release:   2.1
URL:       http://code.google.com/p/otb-sources/wiki/SUMU
License:   MIT
Group:     System Environment/Base
Source0:   login-theme-sumu.tar.gz
BuildArch: noarch

%description
A default GDM theme for gdm-2.16.0 for SUMU by
Open Technologies Bulgaria, Ltd. <http://otb.bg>.

%prep
%setup -q -n login-theme-sumu

%build

%install
rm -rf %{buildroot}
# install data file under standard location
mkdir -p %{buildroot}/%{_datadir}/gdm/themes/SUMU
for f in `find src/ -type f -not -name RHEL.xml`; do
    install -m 0644 $f %{buildroot}/%{_datadir}/gdm/themes/SUMU
done

# install RHEL.xml in /etc and create a symlink
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}
install -m 0644 src/RHEL.xml %{buildroot}/%{_sysconfdir}/%{name}/SUMU.xml
ln -s %{_sysconfdir}/%{name}/SUMU.xml %{buildroot}/%{_datadir}/gdm/themes/SUMU/SUMU.xml

%clean
rm -rf %{buildroot}

%files
%config(noreplace) %{_sysconfdir}/%{name}/SUMU.xml
%{_datadir}/gdm/themes/SUMU
%doc README COPYING

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.7
- Rebuilt for Fedora
* Mon Feb 28 2011 Alexander Todorov <atodorov@NO-SPAM.otb.bg> 3.0.7-1.el6otb
- Use fixed image width for better display on different resolutions
* Wed Feb 09 2011 Alexander Todorov <atodorov@NO-SPAM.otb.bg> 3.0.6-1.el6otb
- add text label to the login screen to display hostname and display number
- update screenshot
* Tue Nov 02 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> 3.0.5-2.el6otb
- use el6otb as dist tag
* Fri Oct 29 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> 3.0.5-1
- Place only RHEL.xml under /etc/
* Fri Oct 29 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> 3.0.4-1
- move the theme files under /etc and create a symbolic link
  this makes it easy to edit the theme without overriding it
* Thu Oct 21 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> 3.0.3-1
- update the main image
* Mon Sep 13 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> 3.0.2-1
- remove logo and background
- update the main image
- scale down icons to 32x32
- update screenshot
* Mon Sep 13 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> 3.0.1-1
- initial revision
