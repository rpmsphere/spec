Name:           hdepanel
Version:        1.0.5git
Release:        1
Summary:        Qt5 based panel based on QtPanel
License:        GPL2
Group:          User Interface/X
URL:            https://github.com/developing4all/hdepanel
Source0:        %{name}-master.zip
BuildRequires:  qt5-devel

%description
Very light Beautiful look. Multiple panels Multple screen support Xdg
compatible Per panel configuration dialog Support for plugins.

%prep
%setup -q -n %{name}-master
sed -i 's|/usr/lib/hde/panel|%{_libdir}/%{name}|' lib/appletslistdialog.cpp lib/panelwindow.cpp

%build
%qmake_qt5
make

%install
mkdir -p %{buildroot}%{_bindir}
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_libdir}/%{name}/plugins
mv lib%{name}* %{buildroot}%{_libdir}
mv plugins/lib*.so %{buildroot}%{_libdir}/%{name}/plugins

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc LICENSE README.md
%{_bindir}/%{name}
%{_libdir}/lib%{name}*
%{_libdir}/%{name}

%changelog
* Fri Mar 06 2020 Wei-Lun Chao <blubat@member.fsf.org> - 1.0.5git
- Rebuilt for Fedora
