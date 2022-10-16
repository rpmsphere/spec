Name:           qtpanel
Version:        0.20130722
Release:        1
Summary:        A very cute panel
License:        GPL3
Group:          User Interface/X
URL:            https://github.com/ixxra/qtpanel/tree/qt5-subdirs
Source0:        %{name}-qt5-subdirs.zip
BuildRequires:  qt5-qtbase-devel
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-wm-devel

%description
A project to create useful and beautiful panel in Qt.

%prep
%setup -q -n %{name}-qt5-subdirs
sed -i '/XCB/d' CMakeLists.txt

%build
cmake . -DCMAKE_INSTALL_PREFIX=/usr -DXCB_XCB_LIBRARIES="-lxcb -lxcb-icccm"
make

%install
mkdir -p %{buildroot}%{_bindir}
install -Dm755 src/%{name} %{buildroot}%{_bindir}/%{name}

%files
%doc README
%{_bindir}/%{name}

%changelog
* Sun Oct 02 2022 Wei-Lun Chao <blubat@member.fsf.org> - 0.20130722
- Rebuild for Fedora
