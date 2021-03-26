%define theme_name Titanium

Summary: %{theme_name} icon theme
Name: titanium-icon-theme
Version: 0.pre1
Release: 7.1
License: CC-BY-NC-ND 3.0
URL: http://code933k.deviantart.com/art/Titanium-Icon-Theme-PRE1-83203913
Group: User Interface/Desktops
Source0: http://www.deviantart.com/download/83203913/titanium_icon_theme_pre1_by_code933k.7z
SOurce1: %{theme_name}-index.theme
BuildArch: noarch
BuildRequires: p7zip

%description
It is just a first pre-release (name it a DRAFT).

%prep
%setup -q -n %{theme_name}
cp %{SOURCE1} index.theme

%build
for i in `find . -name *.svgz`
do
if file "$i"|grep FAT
then
gunzip -S .svgz "$i"
#gzip -S .svgz ${i%.svgz}
mv ${i%.svgz} "$i"
fi
done

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/icons/%{theme_name}
cp -a index.theme scalable %{buildroot}%{_datadir}/icons/%{theme_name}

%clean
rm -rf %{buildroot}

%files
%doc *.txt
%{_datadir}/icons/%{theme_name}

%changelog
* Fri Sep 09 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.pre1
- Rebuild for Fedora
