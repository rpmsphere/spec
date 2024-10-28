Name:           weatherspect
Version:        1.11
Release:        3.1
Summary:        A weather animation in ASCII art
License:        GPL
Group:          Toys
URL:            https://robobunny.com/projects/weatherspect/html/
Source0:        https://robobunny.com/projects/weatherspect/%{name}_v%{version}.tar.gz
Requires:       perl-Term-Animation
BuildArch:      noarch

%description
WeatherSpect is a weather animation in ASCII art. This program uses
weather data supplied by the Weather::Underground module to create
an ASCII animation thatsimulates the weather.

%prep
%setup -q -n %{name}_v%{version}

%install
install -Dm 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%doc CHANGES README gpl.txt
%{_bindir}/%{name}

%changelog
* Sun Feb 22 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.11
- Rebuilt for Fedora
* Sun Nov 24 2013 filipesaraiva <filipesaraiva> 1.11-1.mga4
+ Revision: 552720
- imported package weatherspect

