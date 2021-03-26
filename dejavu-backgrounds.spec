Name:           dejavu-backgrounds
Version:        2012
Release:        4.1
Summary:        Dejavu backgrounds
Group:          User Interface/Desktop
License:        freeware
Source0:        dejavu-backgrounds.zip
Source1:        %{name}.xml
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

%description
Simon Goldin and Jakob Senneby, http://www.goldinsenneby.com/gs/
G. Donald Bain, http://360panos.com/Nevada/NorthAndCentralNevada/PyramidLake/
Sean MacDonald, http://sportsroadtrips.blogspot.tw/2012/04/hnd-cts-april-5-2012.html
nyolc8, http://nyolc8.deviantart.com/art/iDrops-Wallpaper-173437705
http://good-wallpapers.com/movies/2943

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/dejavu
cp * $RPM_BUILD_ROOT/%{_datadir}/backgrounds/dejavu
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/%{name}.xml
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/mate-background-properties/%{name}.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/backgrounds/dejavu
%{_datadir}/*-background-properties/%{name}.xml

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2012
- Rebuild for Fedora
