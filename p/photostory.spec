%define __python /usr/bin/python2
Name:           photostory
Version:        1.0
Release:        1
Summary:        Daily photograph manager
Group:          Applications/Graphics
License:        GPL v3
URL:            http://launchpad.net/photostory
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:	pygtk2, python2-gstreamer

%description
Photostory lets you use your webcam to take a photo of yourself every day,
then compile the photos into a video.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}*
 
%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/photostory
%{_bindir}/photostory_reminder
%{_sysconfdir}/xdg/autostart/photostory_reminder.desktop
%{_datadir}/pixmaps/photostory.svg
%{python_sitelib}/Photostory-*
%{_datadir}/applications/photostory.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
