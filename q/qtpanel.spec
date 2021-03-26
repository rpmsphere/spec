Name:           qtpanel
Version:        0.20130224
Release:        1
Summary:        A very cute panel
License:        GPL3
Group:          User Interface/X
URL:            https://github.com/MadFishTheOne/qtpanel
Source0:        %{name}-master.zip
BuildRequires:  qt4-devel

%description
A project to create useful and beautiful panel in Qt.

%prep
%setup -q -n %{name}-master

%build
%cmake .
make

%install
mkdir -p %{buildroot}%{_bindir}
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Thu Jan 02 2020 Wei-Lun Chao <blubat@member.fsf.org> - 0.20130224
- Rebuild for Fedora
