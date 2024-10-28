%global _name keyboard

Summary:        Hook and simulate global keyboard events
Name:           python3-%{_name}
Version:        0.13.5
Release:        1
License:        MIT
Group:          Development/Tools
Source0:        https://github.com/boppreh/keyboard/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
URL:            https://github.com/boppreh/keyboard
BuildArch:      noarch

%description
Take full control of your keyboard with this small Python library. Hook global
events, register hotkeys, simulate key presses and much more.

%prep
%setup -q -n %{_name}-%{version}

%build
python3 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python3 setup.py install --prefix=/usr --root=%{buildroot} --skip-build

%files
%doc CHANGES.md LICENSE.txt README.md
%{python3_sitelib}/%{_name}*

%changelog
* Sun Oct 10 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.13.5
- Rebuilt for Fedora
