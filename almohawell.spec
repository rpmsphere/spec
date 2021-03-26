Name: almohawell
Summary: Convert and install rpm , deb , tgz and other packages
Version: 9.3.1
Release: 3.1
Group: Utilities/File
License: Waqf
URL: https://sourceforge.net/projects/almohawell/
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildArch: noarch

%description -l ar
بفضل الله ومشيئته تم التوصل إلى إنتاج برنامج المحول .
برنامج المحول هو تفريعة من برنامج الاين ، كما أنه هو نسخة مطورة من برنامج ألماسه
ألاين المخصص للتحويل بين الحزم ،
ويتميز برنامج المحول بالعديد من الخصائص والمزايا الجديدة والتي لا تتوفر في أسلافه
ويدعم المحول تحويل وتثبيت العديد من الحزم منها الردهاتية والسلاكويرية و الديبيانية

يأمل مشروع ألماسه أن يكون قد وفقه الله في إضافة برنامج مميز يؤدي المهمة ، ويلخص
على المطورين مسألة إنتاج حزم احترافية لبرامجهم لتوزيعات متعددة بضغطة زر واحدة .
المحول كبرنامج متكامل يخضع لبنود رخصة وقف .
برنامج ألاين الأصلي نشر برخصة GPL2+ بواسطة جوي هس ضمن مشروع ديبيان .

%description
We thank Allah to help us to write this program almohawell.
Almohawell is a fork of alien program , and it's a developed copy of
Almasa alien which written to convert between packages.
Almohawell has many features which not found on alien and Almasa alien
Almohawell support many types of packages like rpm , tgz , deb .. for
convert and install.

Almohawell by Almasa project as a whole program published under Waqf license .
Origin alien published under GPL2+ license By Joey Hess at Debian project.

%prep
%setup -q -n %{name}

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc copyright
%{_bindir}/%{name}
%{_prefix}/lib/Almohawell/Almohawell/Package.pm
%{_prefix}/lib/Almohawell/Almohawell/Package/Deb.pm
%{_prefix}/lib/Almohawell/Almohawell/Package/Lsb.pm
%{_prefix}/lib/Almohawell/Almohawell/Package/Pkg.pm
%{_prefix}/lib/Almohawell/Almohawell/Package/Rpm.pm
%{_prefix}/lib/Almohawell/Almohawell/Package/Slp.pm
%{_prefix}/lib/Almohawell/Almohawell/Package/Tgz.pm

%changelog
* Fri Mar 31 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 9.3.1
- Rebuild for Fedora
* Thu Jan 17 2013 by Mosaab Hosni Alzoubi <moceap@hotmail.com>
- packed by Almohazzem 0.3.1 (simple RPM packager)
