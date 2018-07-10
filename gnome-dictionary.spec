%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

%define api	1.0
%define major	9
%define libname	%mklibname gdict %{api} %{major}
%define devname	%mklibname -d gdict %{api}

Summary:	GNOME Dictionary
Name:		gnome-dictionary
Epoch:		1
Version:	3.18.0
Release:	2
License:	GPLv2+ and LGPLv2
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-dictionary/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(glib-2.0) >= 2.28.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.0
Conflicts:	gnome-utils < 1:3.3.2

%description
GNOME Dictionary - Look up words in dictionary sources.

%package -n %{libname}
Group:		System/Libraries
Summary:	GNOME dictionary shared library

%description -n %{libname}
This is the shared library required by the GNOME Dictionary.

%package -n %{devname}
Group:		Development/C
Summary:	GNOME dictionary library development files
Requires:	%{libname} = %{EVRD}
Provides:	libgdict%{api}-devel = %{EVRD}

%description -n %{devname}
This is the shared library required by the GNOME Dictionary.

%prep
%setup -q

%build
%configure \
	--disable-schemas-compile
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc README NEWS AUTHORS TODO
%{_bindir}/%{name}
%{_datadir}/gdict-%{api}/
%{_datadir}/glib-2.0/schemas/org.gnome.dictionary.gschema.xml
%{_datadir}/applications/org.gnome.Dictionary.desktop
%{_datadir}/appdata/org.gnome.Dictionary.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Dictionary.service
%{_mandir}/man1/%{name}.1.*

%files -n %{libname}
%{_libdir}/libgdict-%{api}.so.%{major}*

%files -n %{devname}
%doc %{_datadir}/gtk-doc/html/gdict/
%{_libdir}/libgdict-%{api}.so
%{_libdir}/pkgconfig/gdict-%{api}.pc
%{_includedir}/gdict-%{api}

