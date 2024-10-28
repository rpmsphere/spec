Name:           acityofcathay-qing-backgrounds
Version:        2013
Release:        4.1
Summary:        Backgrounds from a chinese panoramic painting
Group:          User Interface/Desktops
License:        Unknown
URL:            https://en.wikipedia.org/wiki/Along_the_River_During_the_Qingming_Festival
Source0:        acityofcathay-qing.zip
BuildArch:      noarch

%description
A remake version of the "A City of Cathay" by five Qing Dynasty court
painters(Chen Mu, Sun Hu, Jin Kun, Dai Hong and Cheng Zhidao) was presented
to the Emperor Qianlong on January 15, 1737.

%prep
%setup -q -n acityofcathay-qing

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/acityofcathay-qing
cp default.jpg default.xml *.svg $RPM_BUILD_ROOT/%{_datadir}/backgrounds/acityofcathay-qing
install -Dm644 %{name}.xml $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/%{name}.xml
install -Dm644 %{name}.xml $RPM_BUILD_ROOT%{_datadir}/mate-background-properties/%{name}.xml

%files
%{_datadir}/backgrounds/acityofcathay-qing
%{_datadir}/*-background-properties/%{name}.xml

%changelog
* Sun Jun 09 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2013
- Rebuilt for Fedora
