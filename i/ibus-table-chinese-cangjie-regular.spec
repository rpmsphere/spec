%global ibus_tables_dir %{_datadir}/ibus-table/tables
%global ibus_icons_dir %{_datadir}/ibus-table/icons

Name:           ibus-table-chinese-cangjie-regular
Version:        2024.5
Release:        1
Summary:        Regular Cangjie Chinese input table for IBus
License:        Public Domain
URL:            https://github.com/chinese-opendesktop/cin-tables
Source0:        cangjie-regular.txt
Source1:        cangjie-regular.png
BuildRequires:  ibus-table
Requires:       ibus-table
BuildArch:      noarch

%description
Regular Cangjie Chinese input table for IBus.

%prep
%setup -qcT
cp %{SOURCE0} %{SOURCE1} .

%build
ibus-table-createdb -n cangjie-regular.db -s cangjie-regular.txt

%install
rm -rf %{buildroot}
install -Dm644 cangjie-regular.png %{buildroot}%{ibus_icons_dir}/cangjie-regular.png
install -Dm644 cangjie-regular.db %{buildroot}%{ibus_tables_dir}/cangjie-regular.db

%files
%{ibus_icons_dir}/cangjie-regular.png
%{ibus_tables_dir}/cangjie-regular.db

%changelog
* Wed May 1 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 2024.5
- Rebuilt for Fedora
