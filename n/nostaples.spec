%undefine _debugsource_packages
%define pkg_name NoStaples

Name: nostaples
Version: 0.3.0
Release: 1
License: GPL
Group: Applications/Multimedia
Summary: User-friendly desktop scanning application
Source: %{name}-%{version}.tar.gz
URL: http://www.etlafins.com/nostaples
Requires: pygtk2, pygtk2-libglade, python-saneme, python-reportlab, python-gtkmvc
BuildArch: noarch

%description
NoStaples aims to be a user-friendly desktop scanning application with
an emphasis on low-volume to medium-volume document archival for small
businesses and home offices. It is written in Python using PyGTK and
Glade with an eye to clear, intelligible code.

%prep
%setup -q
echo -e 'Name[zh_TW]=無針掃描\nComment[zh_TW]=NoStaples 掃描前端程式' >> data/%{name}.desktop 

%build
python2 setup.py build

%install
%__rm -rf %{buildroot}
python2 setup.py install --root=%{buildroot}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean
%__rm -rf %{buildroot}

%files
%doc COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{python2_sitelib}/%{name}*

%changelog
* Wed Mar 14 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.0
- Rebuilt for Fedora
