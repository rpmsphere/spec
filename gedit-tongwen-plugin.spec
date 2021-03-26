Name: gedit-tongwen-plugin
Version: 0.2.4
Release: 1
Summary: Gedit plugin for New Tong Wen Tang
Group: Applications/Editors
License: GPLv2+
URL: http://code.google.com/p/tongwen-python/
Source0: http://tongwen-python.googlecode.com/files/tongwen_gedit-%{version}.tar.gz
Requires: gedit
BuildArch: noarch

%description
This gedit plugin converts between traditional/simplified chinese.
Based on new TongWenTang Firefox add-on.

%prep
%setup -q -n tongwen_gedit-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/gedit-2/plugins/tongwentang
cp tongwentang.gedit-plugin %{buildroot}%{_libdir}/gedit-2/plugins
cp tongwentang/*.py tongwentang/*.xml tongwentang/*.glade %{buildroot}%{_libdir}/gedit-2/plugins/tongwentang
mkdir -p %{buildroot}%{_datadir}
cp -a tongwentang/locale %{buildroot}%{_datadir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/gedit-2/plugins/tongwentang*
%{_datadir}/locale/*/LC_MESSAGES/tongwen_gedit.mo

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuild for Fedora
* Mon May 16 2011 Wei-Lun Chao <bluebat@member.fsf.org> 0.2.4
- Initial RPM package
