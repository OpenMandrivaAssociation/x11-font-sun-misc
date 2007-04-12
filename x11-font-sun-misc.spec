Name: x11-font-sun-misc
Version: 1.0.0
Release: %mkrel 4
Summary: Xorg X11 font sun-misc
Group: Development/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/font/font-sun-misc-%{version}.tar.bz2
License: CHECK
BuildRoot: %{_tmppath}/%{name}-root
BuildArch: noarch

BuildRequires: x11-font-util >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

Conflicts: xorg-x11 <= 6.9.0
PreReq: mkfontdir
PreReq: mkfontscale

%description
Xorg X11 font sun-misc

%prep
%setup -q -n font-sun-misc-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir} --with-fontdir=%_datadir/fonts/misc

%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%_datadir/fonts/misc/fonts.dir
rm -f %{buildroot}%_datadir/fonts/misc/fonts.scale

%post
mkfontscale %_datadir/fonts/misc
mkfontdir %_datadir/fonts/misc

%postun
mkfontscale %_datadir/fonts/misc
mkfontdir %_datadir/fonts/misc

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_datadir/fonts/misc/olcursor.pcf.gz
%_datadir/fonts/misc/olgl*.pcf.gz


