%global _vpath_srcdir contrib/meson

Name:           lz4
Version:        1.9.4
Release:        1
Summary:        Extremely fast compression algorithm

License:        GPLv2+ AND BSD-2-Clause
URL:            https://lz4.github.io/lz4/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  meson >= 0.43
BuildRequires:  ninja

%description
LZ4 is an extremely fast loss-less compression algorithm, providing compression
speed at 400 MB/s per core, scalable with multi-core CPU. It also features
an extremely fast decoder, with speed in multiple GB/s per core, typically
reaching RAM speed limits on multi-core systems.

%package        libs
Summary:        Libaries for lz4

%description    libs
This package contains the libaries for lz4.

%package        devel
Summary:        Development files for lz4
Requires:       %{name}-libs = %{version}-%{release}

%description    devel
This package contains the header(.h) and library(.so) files required to build
applications using liblz4 library.

%package        static
Summary:        Static library for lz4

%description    static
LZ4 is an extremely fast loss-less compression algorithm. This package
contains static libraries for static linking of applications.

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
%meson \
  -Dprograms=true \
  -Ddefault_library=both \
  %{nil}
%meson_build

%install
%meson_install

# Remove documentation
rm -Rf %{buildroot}%{_mandir}

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%license programs/COPYING
%{_bindir}/lz4
%{_bindir}/lz4c
%{_bindir}/lz4cat
%{_bindir}/unlz4

%files libs
%doc lib/LICENSE
%{_libdir}/liblz4.so.*

%files devel
%{_includedir}/lz4*.h
%{_libdir}/liblz4.so
%{_libdir}/pkgconfig/liblz4.pc

%files static
%doc lib/LICENSE
%{_libdir}/liblz4.a
